#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* narnoldi.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcnep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepnarnoldisetlagpreconditioner_ NEPNARNOLDISETLAGPRECONDITIONER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepnarnoldisetlagpreconditioner_ nepnarnoldisetlagpreconditioner
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepnarnoldigetlagpreconditioner_ NEPNARNOLDIGETLAGPRECONDITIONER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepnarnoldigetlagpreconditioner_ nepnarnoldigetlagpreconditioner
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepnarnoldisetksp_ NEPNARNOLDISETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepnarnoldisetksp_ nepnarnoldisetksp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepnarnoldigetksp_ NEPNARNOLDIGETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepnarnoldigetksp_ nepnarnoldigetksp
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepnarnoldisetlagpreconditioner_(NEP nep,PetscInt *lag, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPNArnoldiSetLagPreconditioner(
	(NEP)PetscToPointer((nep) ),*lag);
}
SLEPC_EXTERN void  nepnarnoldigetlagpreconditioner_(NEP nep,PetscInt *lag, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(lag);
*ierr = NEPNArnoldiGetLagPreconditioner(
	(NEP)PetscToPointer((nep) ),lag);
}
SLEPC_EXTERN void  nepnarnoldisetksp_(NEP nep,KSP ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPNArnoldiSetKSP(
	(NEP)PetscToPointer((nep) ),
	(KSP)PetscToPointer((ksp) ));
}
SLEPC_EXTERN void  nepnarnoldigetksp_(NEP nep,KSP *ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool ksp_null = !*(void**) ksp ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPNArnoldiGetKSP(
	(NEP)PetscToPointer((nep) ),ksp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ksp_null && !*(void**) ksp) * (void **) ksp = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
