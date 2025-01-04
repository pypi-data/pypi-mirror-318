#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* nepsolve.c */
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
#define nepsolve_ NEPSOLVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsolve_ nepsolve
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepprojectoperator_ NEPPROJECTOPERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepprojectoperator_ nepprojectoperator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepapplyfunction_ NEPAPPLYFUNCTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepapplyfunction_ nepapplyfunction
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepapplyadjoint_ NEPAPPLYADJOINT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepapplyadjoint_ nepapplyadjoint
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepapplyjacobian_ NEPAPPLYJACOBIAN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepapplyjacobian_ nepapplyjacobian
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetiterationnumber_ NEPGETITERATIONNUMBER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetiterationnumber_ nepgetiterationnumber
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetconverged_ NEPGETCONVERGED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetconverged_ nepgetconverged
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetconvergedreason_ NEPGETCONVERGEDREASON
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetconvergedreason_ nepgetconvergedreason
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgeteigenpair_ NEPGETEIGENPAIR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgeteigenpair_ nepgeteigenpair
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetlefteigenvector_ NEPGETLEFTEIGENVECTOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetlefteigenvector_ nepgetlefteigenvector
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgeterrorestimate_ NEPGETERRORESTIMATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgeterrorestimate_ nepgeterrorestimate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepcomputeerror_ NEPCOMPUTEERROR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepcomputeerror_ nepcomputeerror
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepcomputefunction_ NEPCOMPUTEFUNCTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepcomputefunction_ nepcomputefunction
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepcomputejacobian_ NEPCOMPUTEJACOBIAN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepcomputejacobian_ nepcomputejacobian
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepsolve_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSolve(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepprojectoperator_(NEP nep,PetscInt *j0,PetscInt *j1, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPProjectOperator(
	(NEP)PetscToPointer((nep) ),*j0,*j1);
}
SLEPC_EXTERN void  nepapplyfunction_(NEP nep,PetscScalar *lambda,Vec x,Vec v,Vec y,Mat A,Mat B, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(v);
CHKFORTRANNULLOBJECT(y);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
*ierr = NEPApplyFunction(
	(NEP)PetscToPointer((nep) ),*lambda,
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((v) ),
	(Vec)PetscToPointer((y) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ));
}
SLEPC_EXTERN void  nepapplyadjoint_(NEP nep,PetscScalar *lambda,Vec x,Vec v,Vec y,Mat A,Mat B, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(v);
CHKFORTRANNULLOBJECT(y);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
*ierr = NEPApplyAdjoint(
	(NEP)PetscToPointer((nep) ),*lambda,
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((v) ),
	(Vec)PetscToPointer((y) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ));
}
SLEPC_EXTERN void  nepapplyjacobian_(NEP nep,PetscScalar *lambda,Vec x,Vec v,Vec y,Mat A, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(v);
CHKFORTRANNULLOBJECT(y);
CHKFORTRANNULLOBJECT(A);
*ierr = NEPApplyJacobian(
	(NEP)PetscToPointer((nep) ),*lambda,
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((v) ),
	(Vec)PetscToPointer((y) ),
	(Mat)PetscToPointer((A) ));
}
SLEPC_EXTERN void  nepgetiterationnumber_(NEP nep,PetscInt *its, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(its);
*ierr = NEPGetIterationNumber(
	(NEP)PetscToPointer((nep) ),its);
}
SLEPC_EXTERN void  nepgetconverged_(NEP nep,PetscInt *nconv, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(nconv);
*ierr = NEPGetConverged(
	(NEP)PetscToPointer((nep) ),nconv);
}
SLEPC_EXTERN void  nepgetconvergedreason_(NEP nep,NEPConvergedReason *reason, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetConvergedReason(
	(NEP)PetscToPointer((nep) ),reason);
}
SLEPC_EXTERN void  nepgeteigenpair_(NEP nep,PetscInt *i,PetscScalar *eigr,PetscScalar *eigi,Vec Vr,Vec Vi, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLSCALAR(eigr);
CHKFORTRANNULLSCALAR(eigi);
CHKFORTRANNULLOBJECT(Vr);
CHKFORTRANNULLOBJECT(Vi);
*ierr = NEPGetEigenpair(
	(NEP)PetscToPointer((nep) ),*i,eigr,eigi,
	(Vec)PetscToPointer((Vr) ),
	(Vec)PetscToPointer((Vi) ));
}
SLEPC_EXTERN void  nepgetlefteigenvector_(NEP nep,PetscInt *i,Vec Wr,Vec Wi, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(Wr);
CHKFORTRANNULLOBJECT(Wi);
*ierr = NEPGetLeftEigenvector(
	(NEP)PetscToPointer((nep) ),*i,
	(Vec)PetscToPointer((Wr) ),
	(Vec)PetscToPointer((Wi) ));
}
SLEPC_EXTERN void  nepgeterrorestimate_(NEP nep,PetscInt *i,PetscReal *errest, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLREAL(errest);
*ierr = NEPGetErrorEstimate(
	(NEP)PetscToPointer((nep) ),*i,errest);
}
SLEPC_EXTERN void  nepcomputeerror_(NEP nep,PetscInt *i,NEPErrorType *type,PetscReal *error, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLREAL(error);
*ierr = NEPComputeError(
	(NEP)PetscToPointer((nep) ),*i,*type,error);
}
SLEPC_EXTERN void  nepcomputefunction_(NEP nep,PetscScalar *lambda,Mat A,Mat B, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
*ierr = NEPComputeFunction(
	(NEP)PetscToPointer((nep) ),*lambda,
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ));
}
SLEPC_EXTERN void  nepcomputejacobian_(NEP nep,PetscScalar *lambda,Mat A, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(A);
*ierr = NEPComputeJacobian(
	(NEP)PetscToPointer((nep) ),*lambda,
	(Mat)PetscToPointer((A) ));
}
#if defined(__cplusplus)
}
#endif
