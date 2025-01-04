#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* veccomp.c */
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

#include "slepcvec.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define veccreatecomp_ VECCREATECOMP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define veccreatecomp_ veccreatecomp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define veccreatecompwithvecs_ VECCREATECOMPWITHVECS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define veccreatecompwithvecs_ veccreatecompwithvecs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define veccompsetsubvecs_ VECCOMPSETSUBVECS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define veccompsetsubvecs_ veccompsetsubvecs
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  veccreatecomp_(MPI_Fint * comm,PetscInt Nx[],PetscInt *n,char *t,Vec Vparent,Vec *V, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLINTEGER(Nx);
CHKFORTRANNULLOBJECT(Vparent);
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
/* insert Fortran-to-C conversion for t */
  FIXCHAR(t,cl0,_cltmp0);
*ierr = VecCreateComp(
	MPI_Comm_f2c(*(comm)),Nx,*n,_cltmp0,
	(Vec)PetscToPointer((Vparent) ),V);
  FREECHAR(t,_cltmp0);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
}
SLEPC_EXTERN void  veccreatecompwithvecs_(Vec x[],PetscInt *n,Vec Vparent,Vec *V, int *ierr)
{
PetscBool x_null = !*(void**) x ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(Vparent);
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
*ierr = VecCreateCompWithVecs(x,*n,
	(Vec)PetscToPointer((Vparent) ),V);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! x_null && !*(void**) x) * (void **) x = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
}
SLEPC_EXTERN void  veccompsetsubvecs_(Vec win,PetscInt *n,Vec x[], int *ierr)
{
CHKFORTRANNULLOBJECT(win);
PetscBool x_null = !*(void**) x ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(x);
*ierr = VecCompSetSubVecs(
	(Vec)PetscToPointer((win) ),*n,x);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! x_null && !*(void**) x) * (void **) x = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
