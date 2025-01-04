#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* blopex.c */
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

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsblopexsetblocksize_ EPSBLOPEXSETBLOCKSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsblopexsetblocksize_ epsblopexsetblocksize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsblopexgetblocksize_ EPSBLOPEXGETBLOCKSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsblopexgetblocksize_ epsblopexgetblocksize
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epsblopexsetblocksize_(EPS eps,PetscInt *bs, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSBLOPEXSetBlockSize(
	(EPS)PetscToPointer((eps) ),*bs);
}
SLEPC_EXTERN void  epsblopexgetblocksize_(EPS eps,PetscInt *bs, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(bs);
*ierr = EPSBLOPEXGetBlockSize(
	(EPS)PetscToPointer((eps) ),bs);
}
#if defined(__cplusplus)
}
#endif
